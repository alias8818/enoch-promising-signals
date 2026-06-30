# CPU N-Gram Speculative Decoding for Local Transformer Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-for-local-transformer-serving-af3371cd0af2`
Run ID: `cpu-n-gram-speculative-decoding-for-local-transformer-serving-af3371cd0af2-20260602T200743555113+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6d97d8ae3df8

## What looked useful

The mechanism works on repeated traces but is weak on this natural-text serving proxy; simple unigram drafting matched or beat prompt-local n-gram results, suggesting future work should target repetition-heavy workloads or stronger prompt-lookup baselines.

## Boundaries and scale limits

No real transformer target, no BPE/SentencePiece tokenizer, one natural-text corpus, proxy verifier-call metric rather than end-to-end serving latency, and no production traces such as code/logs/RAG/chat.

## Claim scope

On a regex-tokenized Tiny Shakespeare trace, CPU n-gram drafting is cheap and can exploit deliberately repeated text, but natural-text global and prompt-local traces only reached about 1.08x to 1.10x conservative verifier-call reduction under the tested settings.

## Why it stopped

Proxy/trace-level evidence was insufficient for a paper-positive claim: natural-text n-gram reductions were small and prompt-local n-grams did not consistently beat a unigram control, although repeated-text positive control verified the mechanism.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test real tokenizer and local-serving integration on repetition-heavy code/log/RAG traces with unigram and prompt-lookup controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-tokenizer CPU n-gram speculative decoding on repetition-heavy local-serving traces
- Success threshold: At least one realistic workload shows >=1.25x verifier-call reduction and positive calibrated end-to-end latency after proposer overhead, while beating unigram and prompt-lookup controls.
- Stop condition: Stop if all realistic workloads remain below 1.15x verifier-call reduction or fail to beat the simple controls.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-for-local-transformer-serving-af3371cd0af2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
