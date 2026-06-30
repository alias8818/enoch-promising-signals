# Lookahead-Jacobi Self-Drafting Without External Draft VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lookahead-jacobi-self-drafting-without-external-draft-vram-d27a78320416`
Run ID: `lookahead-jacobi-self-drafting-without-external-draft-vram-d27a78320416-20260614T005300880849+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/600cb3951efe

## What looked useful

Mechanism supported: all Jacobi configurations exactly matched cached greedy outputs, and best configs accepted 2.85 tokens/cycle on distilgpt2 and 2.10 tokens/cycle on gpt2. Practical compute result mixed/negative: best configs still used more target forward calls per token than cached greedy, although wall-clock improved locally by 1.48x-1.70x from fewer decode cycles/Python overhead.

## Boundaries and scale limits

Tested only distilgpt2 and gpt2, short prompts, 16-24 generated tokens, single-request CUDA execution, no fused kernels, no long-context or serving-engine evaluation, no 1B-7B+ models.

## Claim scope

On small GPT-2-class greedy decoding probes, target-model-only Jacobi block self-drafting can preserve exact cached-greedy outputs and accept multiple tokens per verification cycle without loading an external draft model.

## Why it stopped

Bounded local evidence supports the no-external-draft mechanism but not an efficient or paper-positive result: best Jacobi configs remained below the target-forward break-even despite exact outputs and local wall-clock gains.

## Recommended next action

Stop paper path for this implementation; deepen only with a cache-aware or fused Jacobi verifier that must beat cached greedy in target forward-call efficiency on GPT-2-class models before any larger-scale run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-aware Jacobi self-draft verifier for GPT-2-class greedy decoding
- Success threshold: On gpt2 and distilgpt2, exact greedy match for all prompts plus at least 1.10x target forward-call-equivalent efficiency and at least 1.20x wall-clock throughput versus cached greedy.
- Stop condition: Stop if exactness fails, if mean acceptance cannot exceed J+1 after cache-aware optimization, or if forward-call-equivalent efficiency remains below 1.0 on either model.

## Evidence references

- Artifact root: `<local-path>/projects/lookahead-jacobi-self-drafting-without-external-draft-vram-d27a78320416`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
