# Suffix-Tree Speculation from Draft KV Cache for Local LLMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculation-from-draft-kv-cache-for-local-llms-8af75bac7599`
Run ID: `suffix-tree-speculation-from-draft-kv-cache-for-local-llms-8af75bac7599-20260603T215605925212+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3b9552bce518

## What looked useful

Controlled ambiguous synthetic traces showed suffix-tree proposals accepted 2.579 tokens per position versus 2.210 for a unigram cache and near-zero random-cache control. On tiny-gpt2 token traces, suffix proposals accepted only 0.093 tokens per position, so the broad local-LLM speculation claim is not paper-ready.

## Boundaries and scale limits

Synthetic token traces and an sshleifer/tiny-gpt2 prompt probe only; no integrated KV-cache reuse, target batch verification latency, realistic local LLM, or production serving workload was measured.

## Claim scope

A suffix continuation index built from draft-token traces improves accepted-token yield over a unigram continuation cache only when repeated contexts require multi-token disambiguation; a tiny transformer token probe showed only a weak absolute acceptance signal.

## Why it stopped

Proxy/early falsification rather than full validation: synthetic mechanism works under ambiguity, but the real tiny-model acceptance rate is far too low and no end-to-end KV-cache speculative decoder was validated.

## Recommended next action

Stop this run as no-paper useful signal; next concrete test is a bounded integrated speculative decoder on a small real local LLM measuring accepted tokens per verification pass and wall-clock latency against online draft speculation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated Small-LLM Suffix-Cache Speculative Decoder
- Success threshold: At least 1.0 mean accepted suffix-cache tokens per target verification pass and at least 10% wall-clock tokens/sec improvement over online draft speculation on the repeated-context subset, without regression on the non-repeated subset beyond 5%.
- Stop condition: Stop if suffix-cache proposals remain below 0.5 accepted tokens per verification pass or if index/lookup overhead erases latency gains in the small integrated decoder.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculation-from-draft-kv-cache-for-local-llms-8af75bac7599`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
