# Suffix-Tree Prompt-Lookup Draft for Zero-Extra-VRAM Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-prompt-lookup-draft-for-zero-extra-vram-speculation-bf2ff70c20f9`
Run ID: `suffix-tree-prompt-lookup-draft-for-zero-extra-vram-speculation-bf2ff70c20f9-20260610T083641862304+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5157dfaf44e2

## What looked useful

Repeated prompts showed 198x-265x lower lookup latency than naive scans at 32k tokens with about 5 accepted tokens per 8-token draft; high-entropy Markov-like and random controls produced zero useful drafts under tested 4-token and 8-token contexts.

## Boundaries and scale limits

Tested only synthetic token streams up to 131072 prompt tokens with Python CPU data structures; no transformer verifier, no real tokenizer corpus, no GPU serving loop, and no VRAM telemetry beyond the fact that no GPU/model state was allocated.

## Claim scope

CPU-side suffix/ngram prompt indexing can reproduce naive prompt-lookup candidates much faster on repeated-context synthetic prompts and requires no model VRAM, but this run does not validate end-to-end speculative decoding speedup.

## Why it stopped

Proxy/local mechanism probe only: it supports repeated-context lookup efficiency but early-falsifies broad usefulness on high-entropy prompts and lacks direct model-serving evidence.

## Recommended next action

Run a bounded real-model follow-up that integrates CPU prompt lookup into decoding for long-context repeated-document tasks and measures tokens/sec, acceptance rate, CPU overhead, and VRAM.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU prompt-lookup speculation on repeated long-context model prompts
- Success threshold: At least 10% end-to-end tokens/sec improvement on repeated long-context workloads with no measurable VRAM increase and no regression beyond 3% on high-entropy controls.
- Stop condition: Stop if acceptance remains below 1 token per draft on real repeated workloads or CPU lookup overhead erases throughput gains versus baseline decoding.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-prompt-lookup-draft-for-zero-extra-vram-speculation-bf2ff70c20f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
