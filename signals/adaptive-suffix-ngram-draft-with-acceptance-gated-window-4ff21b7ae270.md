# Adaptive Suffix-Ngram Draft with Acceptance-Gated Window

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-suffix-ngram-draft-with-acceptance-gated-window-4ff21b7ae270`
Run ID: `adaptive-suffix-ngram-draft-with-acceptance-gated-window-4ff21b7ae270-20260629T215709336945+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c3f67e44b264

## What looked useful

Adaptive gating was 46.23% worse than fixed_16 and 23.42% worse than fixed_4 on mean target calls per output token. It avoided low-acceptance large windows but was too conservative, using mean window 2.27 and failing to win any tested target-plus-draft cost proxy from alpha 0.005 to 0.5.

## Boundaries and scale limits

Proxy-only evidence: no transformer target, no neural drafter, no natural corpus, no tokenizer/KV-cache/batching effects, and no wall-clock serving throughput measurement. CPU-only run used 12 seeds, 4 synthetic corpora, 8000 tokens per corpus/seed, max ngram 8, and max window 16.

## Claim scope

In a deterministic synthetic oracle-acceptance proxy with suffix-ngram drafting, the tested acceptance-gated adaptive window preserved higher draft acceptance than large fixed windows but did not reduce target calls per output token versus fixed windows.

## Why it stopped

Early proxy falsification, not full validation: the tested adaptive acceptance-gated controller did not beat fixed windows on the primary target-call metric in reproducible synthetic oracle-acceptance tests.

## Recommended next action

Stop this run as no-paper useful signal; only revisit with a direct model-serving benchmark that measures wall-clock tokens/sec and target forward-pass count against fixed-window controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct model-serving benchmark for suffix-ngram adaptive windows
- Success threshold: Adaptive_gated improves wall-clock tokens/sec by at least 10% over the best fixed-window baseline while not increasing target forward-pass count by more than 10% and preserving exact output equivalence.
- Stop condition: Stop if adaptive_gated is slower than the best fixed window on two representative corpora or if implementation overhead dominates and target-call savings are absent.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-suffix-ngram-draft-with-acceptance-gated-window-4ff21b7ae270`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
