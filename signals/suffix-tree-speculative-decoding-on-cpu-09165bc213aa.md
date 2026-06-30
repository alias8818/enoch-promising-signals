# Suffix-Tree Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-on-cpu-09165bc213aa`
Run ID: `suffix-tree-speculative-decoding-on-cpu-09165bc213aa-20260603T210213618844+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8eb4dc190ee9

## What looked useful

Suffix-context speculative drafting is cheap and can work for exact-repetition workloads, reaching 23%-27% target-call reduction on a synthetic copy-burst control. On ordinary prose traces, acceptance is too low for a broad CPU speculative decoding claim, with natural-text mean call reduction stuck near 3.5% across the parameter sweep.

## Boundaries and scale limits

No real LLM logits, no production CPU inference server, no KV-cache or batching measurement, no 1B-7B model validation, and natural-text corpora were small public-domain books. Speedup is idealized from target-call counts with suffix lookup overhead measured separately.

## Claim scope

Bounded CPU trace benchmark of an online suffix-context drafter on three natural-text Project Gutenberg traces plus two synthetic controls. The mechanism reduces target calls on copy-heavy traces but provides only about 3.4%-3.5% mean target-call reduction on ordinary prose under tested settings.

## Why it stopped

Proxy trace-level early falsification for broad prose generation, not a full end-to-end LLM validation; measured natural-text call reduction is too small to justify paper-positive claims.

## Recommended next action

Stop this broad natural-text CPU suffix-tree speculation claim; only run a bounded follow-up if scoped specifically to copy-heavy code/editing/RAG traces with a real CPU LLM verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Suffix-context drafting for copy-heavy CPU LLM workloads
- Success threshold: At least 20% target-call reduction and at least 10% end-to-end latency improvement on two of three copy-heavy workloads, with no regression above 5% on a natural-text control.
- Stop condition: Stop if exact draft acceptance remains below 10% or end-to-end CPU latency improvement is below 5% on the first two copy-heavy workloads.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-on-cpu-09165bc213aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
