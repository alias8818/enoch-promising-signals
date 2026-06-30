# Binary Draft Model with Dense Residual Verifier

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `binary-draft-model-with-dense-residual-verifier-c89dea24a0c2`
Run ID: `binary-draft-model-with-dense-residual-verifier-c89dea24a0c2-20260621T202541963022+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/59f15e12bd75

## What looked useful

The residual-correction mechanism is measurable, but the tested design does not establish an advantage over spending comparable dense capacity directly.

## Boundaries and scale limits

Pure NumPy toy MLP proxy only; no transformer, real corpus, packed binary kernels, latency benchmark, GPT-2-small-class baseline, or large-scale language-model evidence.

## Claim scope

On a small synthetic next-token classification proxy, a dense residual verifier trained on top of a frozen binarized draft MLP recovers about 4.3 percentage points of validation accuracy over the binary draft and produces a net +44 corrected predictions per 1024 validation examples, but it does not beat a dense-only verifier-size control.

## Why it stopped

Bounded proxy evidence is mixed: residual correction improves a binary draft but trails the dense verifier-size control on mean validation accuracy, so the architecture is not paper-positive from this run.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a tiny real sequence model with equal-bit-budget dense controls before considering any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Equal-bit-budget binary draft residual verifier on a tiny real text model
- Success threshold: Binary draft plus dense residual beats the equal-bit-budget dense control by at least 2 percent relative validation loss or 2 absolute accuracy points across the mean of three seeds, without worse than 5 percent throughput or storage-accounting regression versus the declared budget.
- Stop condition: Stop if the residual model fails to beat the equal-bit-budget dense control on two of three seeds or if the dense full baseline cannot learn the task above the draft/control noise floor.

## Evidence references

- Artifact root: `<local-path>/projects/binary-draft-model-with-dense-residual-verifier-c89dea24a0c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
