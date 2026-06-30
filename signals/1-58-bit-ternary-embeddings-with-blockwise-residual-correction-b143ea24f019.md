# 1.58-bit ternary embeddings with blockwise residual correction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-58-bit-ternary-embeddings-with-blockwise-residual-correction-b143ea24f019`
Run ID: `1-58-bit-ternary-embeddings-with-blockwise-residual-correction-b143ea24f019-20260620T193222346921+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a257891428a7

## What looked useful

Blockwise residual mean correction slightly improves MSE, self-cosine, and same-block recall, but after counting fp16 metadata it does not consistently beat a smaller-block scale-only ternary baseline at the same effective bits per dimension.

## Boundaries and scale limits

No pretrained model embeddings, language model embedding tables, packed-kernel latency, or production retrieval corpus was tested. Results are CPU-only synthetic proxy evidence, not full validation.

## Claim scope

Synthetic normalized embedding matrices with Gaussian, clustered, and anisotropic structure at n=4096, dim=768, evaluated by dense-query to quantized-corpus recall@10 and reconstruction metrics across five seeds.

## Why it stopped

Proxy evidence is mixed and not paper-ready: residual correction helps reconstruction but fails the equal-bit retrieval-efficiency test on bounded synthetic embeddings.

## Recommended next action

Run the same bit-budgeted residual-correction versus scale-only controls on real pretrained embedding tables or sentence/document embedding corpora before spending effort on kernels or paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-embedding bit-budget test for blockwise residual ternary correction
- Success threshold: Residual correction improves recall@10 or task retrieval quality by at least 1 percentage point absolute over the matched-bit scale-only baseline on at least two real datasets without worse memory accounting.
- Stop condition: Stop if residual correction again fails to beat matched-bit scale-only controls or only improves reconstruction metrics without retrieval/task gains.

## Evidence references

- Artifact root: `<local-path>/projects/1-58-bit-ternary-embeddings-with-blockwise-residual-correction-b143ea24f019`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
