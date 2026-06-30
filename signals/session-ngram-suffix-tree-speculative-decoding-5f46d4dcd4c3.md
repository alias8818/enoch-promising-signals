# Session-Ngram Suffix-Tree Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `session-ngram-suffix-tree-speculative-decoding-5f46d4dcd4c3`
Run ID: `session-ngram-suffix-tree-speculative-decoding-5f46d4dcd4c3-20260523T054434567893+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/56c9da98cb9d

## What looked useful

Session suffix drafting achieved 2.611x, 8.296x, 6.166x, and 6.472x simulated speedup at draft length 8 on local_docs, local_code, synthetic_logs, and synthetic_chat respectively, beating the static 4-gram control in every primary and draft-length ablation case.

## Boundaries and scale limits

No real LLM, tokenizer-specific serving stack, GPU verification, sampling distribution, KV-cache interaction, latency batching, or quality evaluation was measured. Corpora were local system files plus synthetic repetitive traces capped at 180k tokens per case.

## Claim scope

Bounded CPU-only token-trace proxy: an online session-local longest-suffix n-gram cache reduced simulated target calls versus no draft and a static 4-gram control on local docs, local code, synthetic logs, and synthetic chat traces.

## Why it stopped

Closed as no-paper useful signal because the evidence is a proxy trace benchmark, not direct model-serving validation.

## Recommended next action

Run a bounded real-model follow-up using the same draft source with a small target model/tokenizer and measure end-to-end tokens per second, exact acceptance, latency, and quality against no-draft and static n-gram controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model session suffix draft validation
- Success threshold: Session suffix draft improves end-to-end tokens/s by at least 20% over no-draft and at least 10% over static n-gram on a repetitive workload, without worse quality/regression metrics and with lookup overhead below 5% of total decode time.
- Stop condition: Stop if real-model acceptance fails to produce at least 10% tokens/s improvement over no-draft on two workloads or if lookup/verification overhead erases the simulated target-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/session-ngram-suffix-tree-speculative-decoding-5f46d4dcd4c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
