# Held-out corpus Jacobi n-gram seeding with latency accounting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `held-out-corpus-jacobi-n-gram-seeding-with-latency-account-777b91d7aa`
Run ID: `held-out-corpus-jacobi-n-gram-seeding-with-latency-account-777b91d7aa-20260604T174403310553+0000`

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

- Parent run decision: Jacobi Window Verification with CPU N-gram Seeding: enoch://control-plane/projects/jacobi-window-verification-with-cpu-n-gram-seeding-e188f820c1a8/runs/jacobi-window-verification-with-cpu-n-gram-seeding-e188f820c1a8-20260604T124040993491+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4b3dd5e2c185

## What looked useful

Held-out corpus n-gram seeding has a real but sub-threshold mechanism signal: 206 accepted n-gram proposal tokens out of 1536 emitted tokens, 1.105x speedup versus greedy including lookup overhead, all 64 speculative outputs exactly matched greedy, and random/unigram proposals accepted 0 tokens and were slower than greedy. Parameter ablations stayed below 14% verifier-step reduction.

## Boundaries and scale limits

Test used 64 held-out prompts, 1536 emitted tokens, one small causal LM, greedy decoding, unbatched verifier calls, and a research harness rather than a production KV-cache serving implementation. It did not test large LMs, sampling, batched serving, long contexts, or datacenter-scale throughput.

## Claim scope

On a controlled small direct test using distilgpt2, Wikitext-2 train-split n-gram proposal tables, and held-out Wikitext-2 validation prompts, plain backoff n-gram seeding produced exact greedy-equivalent speculative decoding and improved measured seconds per token by about 10.5% versus greedy after lookup accounting, but reduced verifier steps by only about 13.0%, below the 20% threshold.

## Why it stopped

Controlled direct evidence partially supports the mechanism but fails the stated 20% verifier-step reduction threshold; this is not a full validation or paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should test acceptance-improving proposal ranking before any large-scale serving experiment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Acceptance-ranked held-out n-gram proposals for exact speculative decoding
- Success threshold: Ranked or filtered n-gram proposals must achieve at least 20% verifier-step reduction and at least 10% measured seconds/token speedup versus greedy, while beating the plain n-gram baseline and random/unigram control on the same prompts.
- Stop condition: Stop as negative if the 64-prompt interim remains below 15% verifier-step reduction or if ranking overhead erases the seconds/token gain.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-corpus-jacobi-n-gram-seeding-with-latency-account-777b91d7aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
