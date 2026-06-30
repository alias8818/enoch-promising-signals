# Context-Derived Adaptive N-Gram Speculative Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `context-derived-adaptive-n-gram-speculative-drafting-5d08754a06af`
Run ID: `context-derived-adaptive-n-gram-speculative-drafting-5d08754a06af-20260525T002006152341+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ef73a7cda2a2

## What looked useful

Local frequency within the current context window gave 0.1556 mean accepted tokens versus 0.1386 for static global n-grams (+12.3%), with shuffled-control delta near zero (+0.0046). First-token accuracy was tied and two of three document bootstrap CIs crossed zero.

## Boundaries and scale limits

Six public-domain prose books, three held-out evaluation documents, at most 2500 sampled positions per held-out document, exact text-token matching only; no target LM, no model tokenizer, no verifier latency, and no end-to-end speculative decoding speed measurement.

## Claim scope

On a bounded Project Gutenberg word/punctuation-token proxy benchmark, a context-derived local-frequency n-gram drafter produced a small mean accepted-token lift over a static separate-document n-gram baseline, while a local-recent variant underperformed.

## Why it stopped

Proxy evidence found only a modest mixed signal; this is useful for prioritizing a direct follow-up but is not full validation or paper-ready evidence.

## Recommended next action

Run one bounded direct LM-integrated follow-up using a small causal LM tokenizer/verifier and require accepted model-token drafts plus wall-clock speedup versus no drafting and static n-gram controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Direct Test of Context-Derived Local-Frequency N-Gram Drafting
- Success threshold: At least 10% wall-clock decoding throughput improvement over no drafting and at least 5% mean accepted-token improvement over static n-gram drafting on repetitive long-context prompts, without regression greater than 3% on non-repetitive prompts.
- Stop condition: Stop as negative if local-frequency drafting does not improve accepted model tokens per verifier call over static n-grams or if verifier overhead eliminates wall-clock gains.

## Evidence references

- Artifact root: `<local-path>/projects/context-derived-adaptive-n-gram-speculative-drafting-5d08754a06af`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
