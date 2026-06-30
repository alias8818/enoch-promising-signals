# CPU N-Gram Prompt-Lookup Spec Decode vs Greedy

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-prompt-lookup-spec-decode-vs-greedy-c7b6ab8375ec`
Run ID: `cpu-n-gram-prompt-lookup-spec-decode-vs-greedy-c7b6ab8375ec-20260628T221022959668+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cd046c842bf8

## What looked useful

Prompt-lookup speculation reduced target calls by up to 81.8% and improved speed up to 3.46x on copy-heavy traces, but regressed to 0.93x in zero-overlap configurations. CPU use should be gated by overlap/copy likelihood.

## Boundaries and scale limits

No neural language model was run; target-model cost was proxied with deterministic CPU work. Results should not be read as end-to-end CPU LLM throughput evidence.

## Claim scope

Deterministic CPU protocol benchmark shows prompt-lookup speculative decoding can exactly match greedy traces and improve wall time when generated continuations copy prompt spans, but provides little or no benefit when prompt overlap is absent.

## Why it stopped

Useful proxy/protocol evidence was produced, but it is not full validation and is not paper-ready without real CPU model logits and KV-cache timing.

## Recommended next action

Stop this run as bounded proxy evidence; next concrete test is an end-to-end CPU benchmark with a small real causal LM and the same copy-heavy, mixed, and no-overlap controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU prompt-lookup speculative decoding on a small causal LM
- Success threshold: At least 1.25x median end-to-end speedup on copy-heavy prompts with exact greedy-equivalent outputs and no more than 5% slowdown on no-overlap prompts when the gate is enabled.
- Stop condition: Stop if real-model speculative decoding fails exact equivalence, copy-heavy speedup is below 1.10x, or the overlap gate cannot avoid no-overlap regressions.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-prompt-lookup-spec-decode-vs-greedy-c7b6ab8375ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
