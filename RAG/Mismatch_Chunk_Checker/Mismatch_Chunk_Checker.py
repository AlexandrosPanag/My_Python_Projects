# Created by Alexandros Panagiotakopoulos
# alexandrospanag.github.io
# CC BY-SA 4.0
# Date: 28-11-2025

"""
MISMATCH CHUNK CHECKER
======================
This script analyzes the English and Greek knowledge bases to identify missing chunks
and discrepancies between the two versions.

Features:
- Identifies chunks present in one KB but missing in the other
- Checks for different chunk IDs between languages
- Reports chunk count differences
- Provides detailed mismatch analysis
- Generates a comprehensive report with statistics
"""

import re
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple


class KnowledgeBaseAnalyzer:
    """Analyzes knowledge base files for chunk mismatches."""
    
    def __init__(self, en_file: str, el_file: str):
        """
        Initialize the analyzer with file paths.
        
        Args:
            en_file: Path to English knowledge base file
            el_file: Path to Greek knowledge base file
        """
        self.en_file = en_file
        self.el_file = el_file
        self.en_chunks = {}
        self.el_chunks = {}
        self.en_chunk_ids = set()
        self.el_chunk_ids = set()
        
    def extract_chunks(self, content: str) -> Dict[str, Dict]:
        """
        Extract all chunks from knowledge base content.
        
        Args:
            content: File content as string
            
        Returns:
            Dictionary with chunk_id as key and chunk info as value
        """
        chunks = {}
        # Pattern to find chunk dictionaries
        chunk_pattern = r"'chunk_id':\s*'([^']+)'.*?'chunk_topic':\s*'([^']+)'.*?'questions':\s*\[(.*?)\].*?'answer':"
        
        for match in re.finditer(chunk_pattern, content, re.DOTALL):
            chunk_id = match.group(1)
            chunk_topic = match.group(2)
            questions_str = match.group(3)
            
            chunks[chunk_id] = {
                'topic': chunk_topic,
                'questions_count': len(re.findall(r'"[^"]*"', questions_str))
            }
        
        return chunks
    
    def extract_chunk_blocks(self, content: str) -> Dict[str, Dict]:
        """
        Extract CHUNK_* variable definitions.
        
        Args:
            content: File content as string
            
        Returns:
            Dictionary with chunk block name as key
        """
        chunk_blocks = {}
        # Pattern to find CHUNK_* = [ ... ]
        block_pattern = r"(CHUNK_[A-Z_]+)\s*=\s*\[(.*?)\n\]"
        
        for match in re.finditer(block_pattern, content, re.DOTALL):
            block_name = match.group(1)
            block_content = match.group(2)
            
            # Extract chunk IDs from this block
            chunk_ids = re.findall(r"'chunk_id':\s*'([^']+)'", block_content)
            chunk_blocks[block_name] = {
                'chunk_ids': chunk_ids,
                'count': len(chunk_ids)
            }
        
        return chunk_blocks
    
    def load_knowledge_bases(self):
        """Load both knowledge base files and extract chunks."""
        try:
            with open(self.en_file, 'r', encoding='utf-8') as f:
                en_content = f.read()
            
            with open(self.el_file, 'r', encoding='utf-8') as f:
                el_content = f.read()
            
            self.en_chunks = self.extract_chunks(en_content)
            self.el_chunks = self.extract_chunks(el_content)
            self.en_chunk_blocks = self.extract_chunk_blocks(en_content)
            self.el_chunk_blocks = self.extract_chunk_blocks(el_content)
            
            self.en_chunk_ids = set(self.en_chunks.keys())
            self.el_chunk_ids = set(self.el_chunks.keys())
            
            print("✓ Knowledge bases loaded successfully")
            print(f"  English chunks found: {len(self.en_chunk_ids)}")
            print(f"  Greek chunks found: {len(self.el_chunk_ids)}")
            
        except FileNotFoundError as e:
            print(f"✗ Error: File not found - {e}")
            raise
        except Exception as e:
            print(f"✗ Error loading files: {e}")
            raise
    
    def find_missing_chunks(self) -> Dict:
        """
        Identify missing chunks between versions.
        
        Returns:
            Dictionary with missing chunks information
        """
        missing = {
            'in_greek_only': self.el_chunk_ids - self.en_chunk_ids,
            'in_english_only': self.en_chunk_ids - self.el_chunk_ids,
            'in_both': self.en_chunk_ids & self.el_chunk_ids
        }
        
        return missing
    
    def analyze_chunk_blocks(self) -> Dict:
        """
        Compare chunk blocks between versions.
        
        Returns:
            Dictionary with block comparison information
        """
        analysis = {
            'en_blocks': set(self.en_chunk_blocks.keys()),
            'el_blocks': set(self.el_chunk_blocks.keys()),
        }
        
        analysis['blocks_in_both'] = analysis['en_blocks'] & analysis['el_blocks']
        analysis['blocks_greek_only'] = analysis['el_blocks'] - analysis['en_blocks']
        analysis['blocks_english_only'] = analysis['en_blocks'] - analysis['el_blocks']
        
        return analysis
    
    def compare_block_sizes(self) -> List[Tuple]:
        """
        Compare chunk counts within matching blocks.
        
        Returns:
            List of tuples (block_name, en_count, el_count, difference)
        """
        differences = []
        
        for block in self.en_chunk_blocks.keys():
            if block in self.el_chunk_blocks:
                en_count = self.en_chunk_blocks[block]['count']
                el_count = self.el_chunk_blocks[block]['count']
                diff = el_count - en_count
                
                if diff != 0:
                    differences.append((block, en_count, el_count, diff))
        
        return sorted(differences, key=lambda x: abs(x[3]), reverse=True)
    
    def generate_report(self) -> str:
        """
        Generate a comprehensive mismatch report.
        
        Returns:
            Formatted report string
        """
        report = []
        report.append("=" * 80)
        report.append("KNOWLEDGE BASE MISMATCH ANALYSIS REPORT")
        report.append("=" * 80)
        report.append("")
        
        # Overall statistics
        report.append("📊 OVERALL STATISTICS")
        report.append("-" * 80)
        report.append(f"English chunks:  {len(self.en_chunk_ids):3d}")
        report.append(f"Greek chunks:    {len(self.el_chunk_ids):3d}")
        report.append(f"Difference:      {abs(len(self.en_chunk_ids) - len(self.el_chunk_ids)):3d}")
        report.append(f"Common chunks:   {len(self.en_chunk_ids & self.el_chunk_ids):3d}")
        report.append("")
        
        # Missing chunks analysis
        missing = self.find_missing_chunks()
        
        report.append("❌ MISSING CHUNKS")
        report.append("-" * 80)
        
        if missing['in_greek_only']:
            report.append(f"✓ Chunks in GREEK but NOT in ENGLISH ({len(missing['in_greek_only'])}):")
            for chunk_id in sorted(missing['in_greek_only']):
                topic = self.el_chunks[chunk_id]['topic']
                report.append(f"   • {chunk_id:30s} | {topic}")
            report.append("")
        
        if missing['in_english_only']:
            report.append(f"✓ Chunks in ENGLISH but NOT in GREEK ({len(missing['in_english_only'])}):")
            for chunk_id in sorted(missing['in_english_only']):
                topic = self.en_chunks[chunk_id]['topic']
                report.append(f"   • {chunk_id:30s} | {topic}")
            report.append("")
        
        if not missing['in_greek_only'] and not missing['in_english_only']:
            report.append("✓ No missing chunks - All chunks exist in both versions!")
            report.append("")
        
        # Block analysis
        block_analysis = self.analyze_chunk_blocks()
        report.append("📦 CHUNK BLOCK ANALYSIS")
        report.append("-" * 80)
        report.append(f"English blocks: {len(block_analysis['en_blocks']):2d}")
        report.append(f"Greek blocks:   {len(block_analysis['el_blocks']):2d}")
        report.append("")
        
        if block_analysis['blocks_greek_only']:
            report.append(f"Blocks in GREEK only ({len(block_analysis['blocks_greek_only'])}):")
            for block in sorted(block_analysis['blocks_greek_only']):
                count = self.el_chunk_blocks[block]['count']
                report.append(f"   • {block:30s} ({count} chunks)")
            report.append("")
        
        if block_analysis['blocks_english_only']:
            report.append(f"Blocks in ENGLISH only ({len(block_analysis['blocks_english_only'])}):")
            for block in sorted(block_analysis['blocks_english_only']):
                count = self.en_chunk_blocks[block]['count']
                report.append(f"   • {block:30s} ({count} chunks)")
            report.append("")
        
        # Block size comparison
        size_differences = self.compare_block_sizes()
        if size_differences:
            report.append("📏 BLOCK SIZE DIFFERENCES")
            report.append("-" * 80)
            report.append(f"{'Block Name':<35} {'English':<10} {'Greek':<10} {'Diff':<10}")
            report.append("-" * 80)
            
            for block, en_count, el_count, diff in size_differences:
                diff_indicator = "⬆️ " if diff > 0 else "⬇️ "
                report.append(f"{block:<35} {en_count:<10} {el_count:<10} {diff_indicator}{abs(diff):<8}")
            report.append("")
        
        # Detailed chunk comparison
        report.append("🔍 COMMON CHUNKS DETAILED VIEW")
        report.append("-" * 80)
        
        common_chunks = sorted(missing['in_both'])
        report.append(f"Total common chunks: {len(common_chunks)}")
        report.append("")
        report.append(f"{'Chunk ID':<35} {'English Topic':<40} {'Greek Topic':<40}")
        report.append("-" * 115)
        
        for chunk_id in common_chunks[:20]:  # Show first 20
            en_topic = self.en_chunks[chunk_id]['topic']
            el_topic = self.el_chunks[chunk_id]['topic']
            
            # Truncate long topics
            en_topic = (en_topic[:37] + '...') if len(en_topic) > 40 else en_topic
            el_topic = (el_topic[:37] + '...') if len(el_topic) > 40 else el_topic
            
            report.append(f"{chunk_id:<35} {en_topic:<40} {el_topic:<40}")
        
        if len(common_chunks) > 20:
            report.append(f"... and {len(common_chunks) - 20} more chunks")
        
        report.append("")
        report.append("=" * 80)
        
        # Recommendations
        report.append("💡 RECOMMENDATIONS")
        report.append("-" * 80)
        
        total_diff = abs(len(self.en_chunk_ids) - len(self.el_chunk_ids))
        sync_percentage = (len(missing['in_both']) / max(len(self.en_chunk_ids), len(self.el_chunk_ids))) * 100
        
        report.append(f"Synchronization level: {sync_percentage:.1f}%")
        
        if missing['in_greek_only']:
            report.append(f"→ Translate {len(missing['in_greek_only'])} Greek-only chunks to English")
        
        if missing['in_english_only']:
            report.append(f"→ Translate {len(missing['in_english_only'])} English-only chunks to Greek")
        
        if size_differences:
            report.append(f"→ Review {len(size_differences)} blocks with size differences")
        
        report.append("")
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def export_report_to_file(self, output_file: str):
        """
        Export the report to a text file.
        
        Args:
            output_file: Path to output file
        """
        report = self.generate_report()
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"\n✓ Report exported to: {output_file}")
        except Exception as e:
            print(f"✗ Error exporting report: {e}")
    
    def export_json_report(self, output_file: str):
        """
        Export detailed analysis as JSON.
        
        Args:
            output_file: Path to output JSON file
        """
        missing = self.find_missing_chunks()
        block_analysis = self.analyze_chunk_blocks()
        size_differences = self.compare_block_sizes()
        
        json_report = {
            'summary': {
                'english_chunks': len(self.en_chunk_ids),
                'greek_chunks': len(self.el_chunk_ids),
                'common_chunks': len(missing['in_both']),
                'synchronization_percentage': (len(missing['in_both']) / max(len(self.en_chunk_ids), len(self.el_chunk_ids))) * 100
            },
            'missing_chunks': {
                'in_greek_only': sorted(list(missing['in_greek_only'])),
                'in_english_only': sorted(list(missing['in_english_only']))
            },
            'block_analysis': {
                'english_blocks': len(block_analysis['en_blocks']),
                'greek_blocks': len(block_analysis['el_blocks']),
                'blocks_greek_only': sorted(list(block_analysis['blocks_greek_only'])),
                'blocks_english_only': sorted(list(block_analysis['blocks_english_only']))
            },
            'block_size_differences': [
                {
                    'block': block,
                    'english_count': en_count,
                    'greek_count': el_count,
                    'difference': diff
                }
                for block, en_count, el_count, diff in size_differences
            ]
        }
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(json_report, f, ensure_ascii=False, indent=2)
            print(f"✓ JSON report exported to: {output_file}")
        except Exception as e:
            print(f"✗ Error exporting JSON report: {e}")


def main():
    """Main execution function."""
    print("🔍 KNOWLEDGE BASE MISMATCH CHECKER")
    print("=" * 80)
    print()
    
    # File paths
    en_file = r"C:\Users\alexa\Desktop\knowledge_base_en.py"
    el_file = r"C:\Users\alexa\Desktop\knowledge_base_el.py"
    
    # Check if files exist
    if not Path(en_file).exists():
        print(f"✗ English file not found: {en_file}")
        return
    
    if not Path(el_file).exists():
        print(f"✗ Greek file not found: {el_file}")
        return
    
    # Initialize analyzer
    analyzer = KnowledgeBaseAnalyzer(en_file, el_file)
    
    # Load knowledge bases
    print("Loading knowledge bases...")
    analyzer.load_knowledge_bases()
    print()
    
    # Generate and display report
    report = analyzer.generate_report()
    print(report)
    
    # Export reports
    print("\n📁 Exporting reports...")
    analyzer.export_report_to_file(r"C:\Users\alexa\Desktop\KB_Mismatch_Report.txt")
    analyzer.export_json_report(r"C:\Users\alexa\Desktop\KB_Mismatch_Report.json")
    
    print("\n✓ Analysis complete!")


if __name__ == "__main__":
    main()

