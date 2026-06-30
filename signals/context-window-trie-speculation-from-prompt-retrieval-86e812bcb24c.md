# Context-Window Trie Speculation from Prompt Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `context-window-trie-speculation-from-prompt-retrieval-86e812bcb24c`
Run ID: `context-window-trie-speculation-from-prompt-retrieval-86e812bcb24c-20260531T204009774825+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/211246bfc7ae

## What looked useful

Across 10086 usable examples, no-prefix trie drafting averaged only 0.212 consecutive hits with 95.3% zero-hit cases; with one oracle copied prefix token it averaged 18.226 hits and 0.822 accept rate; with two prefix tokens it averaged 20.311 hits and 0.962 accept rate. A lexical question anchor found the exact answer start only 2.36% of the time and averaged 0.572 consecutive hits, so the trie is useful for continuation after anchoring but not sufficient as a standalone retrieval-to-start mechanism.

## Boundaries and scale limits

Single public extractive QA dataset, regex tokenization rather than a production LLM tokenizer, offline oracle-prefix evaluation instead of live speculative decoding with a model, and no latency/throughput measurement inside an LLM serving stack.

## Claim scope

On SQuAD v1.1 dev extractive-copy spans, a suffix trie built from prompt context drafts long matching continuations once generation is already anchored by one or more copied target tokens, but simple prompt-retrieval lexical anchoring does not reliably find the answer span start.

## Why it stopped

Bounded proxy evidence supports the continuation mechanism but early-falsifies the stronger standalone prompt-retrieval trie claim because start selection from the prompt is weak without an external anchor.

## Recommended next action

Stop this run as no-paper useful signal; next test should attach the trie drafter to model-generated first tokens or top-k span anchors and measure accepted speculative tokens plus latency on real generation traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-anchored prompt-trie speculative decoding on extractive generation traces
- Success threshold: At least 1.5x effective decoding-token reduction or 20% latency reduction on copied-span outputs without changing exact generated text, with gains persisting across at least two QA/citation datasets.
- Stop condition: Stop if model-anchored trie drafting accepts under 2 tokens per drafted segment on average or if anchor/rejection overhead eliminates measured latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/context-window-trie-speculation-from-prompt-retrieval-86e812bcb24c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
