# N-gram suffix speculative decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-speculative-decoding-on-cpu-bb3f5d302453`
Run ID: `n-gram-suffix-speculative-decoding-on-cpu-bb3f5d302453-20260530T005534046934+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6d56167698b4

## What looked useful

Byte-level suffix copying reached 1.445x ideal verifier-call speedup on 50k held-out tokens, but the word-token proxy reached only 1.028x with 90.3% zero-accept proposals, indicating that byte proxy gains may not transfer to practical LLM tokenization.

## Boundaries and scale limits

No real LLM, no BPE tokenizer, no KV-cache integration, one corpus, and ideal verifier-call accounting rather than measured end-to-end decoding wall-clock.

## Claim scope

On Tiny Shakespeare, a newest-match n-gram suffix draft proposer gives a useful ideal verifier-call reduction on byte tokens but only a weak reduction on a word/punctuation token proxy.

## Why it stopped

Early proxy falsification of the broad practical claim: the mechanism works for byte-like tokens but becomes too weak under a word-like token proxy; this is not full validation or a full BPE/runtime rejection.

## Recommended next action

Run a bounded deepen test with a real BPE tokenizer and small CPU LLM runtime before considering any runtime integration or paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE-token n-gram suffix drafting in a small CPU LLM loop
- Success threshold: At least 1.15x end-to-end tokens/sec improvement on one repetitive domain and no worse than 0.98x on ordinary prose, measured over at least 10k generated tokens per condition.
- Stop condition: Stop if BPE-token ideal speedup is below 1.10x on the corpus-level trace or if integrated CPU runtime throughput is below 0.98x versus greedy decoding.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-speculative-decoding-on-cpu-bb3f5d302453`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
